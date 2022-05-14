import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pickle
from sklearn.metrics import roc_auc_score
from tabs.tab_2 import choices
import json
import joblib

Viridis = [
    "#440154", "#440558", "#450a5c", "#450e60", "#451465", "#461969",
    "#461d6d", "#462372", "#472775", "#472c7a", "#46307c", "#45337d",
    "#433880", "#423c81", "#404184", "#3f4686", "#3d4a88", "#3c4f8a",
    "#3b518b", "#39558b", "#37598c", "#365c8c", "#34608c", "#33638d",
    "#31678d", "#2f6b8d", "#2d6e8e", "#2c718e", "#2b748e", "#29788e",
    "#287c8e", "#277f8e", "#25848d", "#24878d", "#238b8d", "#218f8d",
    "#21918d", "#22958b", "#23988a", "#239b89", "#249f87", "#25a186",
    "#25a584", "#26a883", "#27ab82", "#29ae80", "#2eb17d", "#35b479",
    "#3cb875", "#42bb72", "#49be6e", "#4ec16b", "#55c467", "#5cc863",
    "#61c960", "#6bcc5a", "#72ce55", "#7cd04f", "#85d349", "#8dd544",
    "#97d73e", "#9ed93a", "#a8db34", "#b0dd31", "#b8de30", "#c3df2e",
    "#cbe02d", "#d6e22b", "#e1e329", "#eae428", "#f5e626", "#fde725"
]


def display_eval_metrics(value):
    ### Comparison of Possible Models
    if value==choices[0]:
        compare_models=pd.read_csv('resources/compare_models.csv', index_col=0)
        mydata1 = go.Bar(
            x=compare_models.loc['F1 score'].index,
            y=compare_models.loc['F1 score'],
            name=compare_models.index[0],
            marker=dict(color=Viridis[50])
        )
        mydata2 = go.Bar(
            x=compare_models.loc['Accuracy'].index,
            y=compare_models.loc['Accuracy'],
            name=compare_models.index[1],
            marker=dict(color=Viridis[30])
        )
        mydata3 = go.Bar(
            x=compare_models.loc['AUC score'].index,
            y=compare_models.loc['AUC score'],
            name=compare_models.index[2],
            marker=dict(color=Viridis[10])
        )
        mylayout = go.Layout(
            title='DecistionTree has the highest accuracy and ROC-AUC score',
            xaxis=dict(title = 'Predictive models'), # x-axis label
            yaxis=dict(title = 'Score'), # y-axis label

        )
        fig = go.Figure(data=[mydata1, mydata2, mydata3], layout=mylayout)

        # from sklearn import tree
        # import matplotlib.pyplot as plt
        # #plt.rcParams["figure.figsize"] = (20,10)
        # with open('resources/final_dtc_model.pkl', 'rb') as f:
        #     dtc_model = pickle.load(f)
        #
        # #fig = plt.figure(figsize=(25,20))
        # fig = tree.plot_tree(
        #     dtc_model,
        #     feature_names=[
        #         'Siblings and Spouses', 'female', 'Cabin Class 2',
        #         'Cabin Class 3', 'Cherbourg', 'Queenstown', 'Age (20, 28]',
        #         'Age (28, 38]', 'Age (38, 80]', 'Mrs.', 'Miss', 'VIP'],
        #     filled=True)
        return fig

    ### Final Model Metrics
    elif value==choices[1]:
        file = open('resources/eval_scores.pkl', 'rb')
        evals=pickle.load(file)
        file.close()
        mydata = [go.Bar(
            x=list(evals.keys()),
            y=list(evals.values()),
            marker=dict(color=Viridis[::12])
        )]

        mylayout = go.Layout(
            title='Evaluation Metrics for DecisionTree Model (Testing Dataset = 127 passengers)',
            xaxis = {'title': 'Metrics'},
            yaxis = {'title': 'Percent'},

        )
        fig = go.Figure(data=mydata, layout=mylayout)
        return fig

    # Receiver Operating Characteristic (ROC): Area Under Curve
    elif value==choices[2]:
        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=("(ROC/AUC) for Regression Model", "(ROC/AUC) for DecisionTree Model"))
        with open('resources/roc_dict.json') as json_file:
            roc_dict = json.load(json_file)
        with open('resources/roc_dt_dict.json') as json_file:
            roc_dt_dict = json.load(json_file)

        trace0=go.Scatter(
            x=[0,1],
            y=[0,1],
            mode='lines',
            name='Baseline Area: 50.0',
            marker=dict(color=Viridis[50])
        )

        FPR=roc_dict['FPR']
        TPR=roc_dict['TPR']
        y_test=pd.Series(roc_dict['y_test'])
        predictions=roc_dict['predictions']
        roc_score=round(100*roc_auc_score(y_test, predictions),1)
        trace1=go.Scatter(
                x=FPR,
                y=TPR,
                meta="Unsorted Input",
                mode='lines',
                name=f'AUC: {roc_score}',
                marker=dict(color=Viridis[10])
                )

        FPR=roc_dt_dict['FPR']
        TPR=roc_dt_dict['TPR']
        y_test=pd.Series(roc_dt_dict['y_test'])
        predictions=roc_dt_dict['predictions']
        roc_score=round(100*roc_auc_score(y_test, predictions),1)
        trace2=go.Scatter(
            x=FPR,
            y=TPR,
            mode='lines',
            name=f'AUC: {roc_score}',
            marker=dict(color='red',)
        )

        fig.add_trace(trace0, row=1, col=1)
        fig.add_trace(trace1, row=1, col=1)
        fig.add_trace(trace0, row=2, col=1)
        fig.add_trace(trace2, row=2, col=1)
        fig.update_layout(height=1200, width=900)
        return fig

    # Confusion Matrix
    elif value == choices[3]:
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            specs=[[{"type": "table"}], [{"type": "scatter"}]],
            subplot_titles=("Confusion Matrix for Regression Model",
                            "Confusion Matrix for DecisionTree Model"))
        with open('resources/roc_dict.json') as json_file:
            roc_dict = json.load(json_file)
        FPR=roc_dict['FPR']
        TPR=roc_dict['TPR']
        y_test=pd.Series(roc_dict['y_test'])
        
        cm=pd.read_csv('resources/confusion_matrix.csv')
        trace = go.Table(
            header=dict(values=cm.columns,
                        line=dict(color='#7D7F80'),
                        fill=dict(color=Viridis[55]),
                        align=['left'] * 5),
            cells=dict(values=[cm[f'n={len(y_test)}'], cm['pred: survival'], cm['pred: death']],
                       line=dict(color='#7D7F80'),
                       fill=dict(color='white'),
                       align=['left'] * 5))
        fig.add_trace(trace, row=1, col=1)
        # df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv")
        # fig.add_trace(
        #     go.Scatter(
        #         x=df["Date"],
        #         y=df["Mining-revenue-USD"],
        #         mode="lines",
        #         name="mining revenue"
        #     ),
        #     row=2, col=1
        # )

        # Load Confusion Matrix for DecisionTree Model
        with open('resources/cfm_dtm.pkl', 'rb') as f:
            z = pickle.load(f)
        x = ['Pred: Survival', 'Pred: Death']
        y = ['Actual: Survival', 'Actual: Death']
        z_text = [[str(y) for y in x] for x in z]
        fig = ff.create_annotated_heatmap(
            z, x=x, y=y, annotation_text=z_text, colorscale='Viridis')
        # add title
        fig.update_layout(title_text='<b>Confusion matrix for DecisionTree '
                                     'Model</b>',
                          )

        # add custom xaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.15,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # fig custom yaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.35,
                                y=0.5,
                                showarrow=False,
                                text="Actual value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))
        fig['data'][0]['showscale'] = True
        #fig.add_trace(fig, row=2, col=1)
        fig.update_layout(height=400, width=800)
        return fig

    # Odds of Survival (Coefficients)
    elif value==choices[4]:
        coeffs=pd.read_csv('resources/coefficients.csv')
        mydata = [go.Bar(
            x=coeffs['feature'],
            y=coeffs['coefficient'],
            marker=dict(color=Viridis[::-6])
        )]
        mylayout = go.Layout(
            title='Married women in 1st class had better odds of survival, especially if younger than 38',
            xaxis = {'title': 'Passenger Features'},
            yaxis = {'title': 'Odds of Survival'},

        )
        fig = go.Figure(data=mydata, layout=mylayout)
        return fig
