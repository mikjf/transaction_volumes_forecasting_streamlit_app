import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_simulation(data, predictions_df_ar, fitted_df_ar, df_fitted_ETS, df_pred_ETS, df_predictions_pr, df_fitted_pr):
    #DATA -> Month to dateTime
    data['Month'] = pd.Series(pd.date_range(str(data.iloc[0]['Month']), freq="M", periods=len(data['Month'])))
    #AR -> Index to DateTime
    predictions_df_ar.index = pd.Series(pd.date_range(str(predictions_df_ar.index[0]), freq="M", periods=len(predictions_df_ar.index)))
    fitted_df_ar.index = pd.Series(pd.date_range(str(fitted_df_ar.index[0]), freq="M", periods=len(fitted_df_ar.index)))
    #fitted_df_ar['timestamp'] = pd.to_datetime(fitted_df_ar['timestamp'])
    #predictions_df_ar['timestamp'] = pd.to_datetime(predictions_df_ar['timestamp'])
    #ETS -> Index to DateTime
    df_fitted_ETS.index = pd.Series(pd.date_range(str(df_fitted_ETS.index[0]), freq="M", periods=len(df_fitted_ETS.index)))
    df_pred_ETS.index = pd.Series(pd.date_range(str(df_pred_ETS.index[0]), freq="M", periods=len(df_pred_ETS.index)))
    #df_fitted_ETS['timestamp'] = pd.to_datetime(df_fitted_ETS['timestamp'])
    #df_pred_ETS['timestamp'] = pd.to_datetime(df_pred_ETS['timestamp'])
    #PR -> Index to DateTime
    df_predictions_pr.index = pd.Series(pd.date_range(str(df_predictions_pr.index[0]), freq="M", periods=len(df_predictions_pr.index)))
    df_fitted_pr.index = pd.Series(pd.date_range(str(df_fitted_pr.index[0]), freq="M", periods=len(df_fitted_pr.index)))
    #df_fitted_pr['timestamp'] = pd.to_datetime(df_fitted_pr['timestamp'])
    #df_predictions_pr['timestamp'] = pd.to_datetime(df_predictions_pr['timestamp'])

    #CREATING SUBPLOTS
    fig = make_subplots(rows=3, cols=1, subplot_titles=('ARIMA model', 'ETS model', 'PROPHET model'))

    #ARIMA PLOT
    #fig = go.Figure()
    fig.add_traces(
        [go.Scatter(x=data["Month"], y=data['total'], mode='lines+markers', marker=dict(size=10, color='white'),
                    name='Data', legendgroup = '1',
                    #hovertemplate='%{y:.0f}'
                    ),
         go.Scatter(x=fitted_df_ar.index, y=fitted_df_ar['fitted'], mode='lines',
                    marker=dict(size=10, color='lightgreen' ), name='Fitted', legendgroup = '1',
                    #hovertemplate='%{y:.0f}'
                    ),
         go.Scatter(x=predictions_df_ar.index, y=predictions_df_ar.predicted, mode='lines+markers',
                    marker=dict(size=10, color='lightgreen', symbol='triangle-right'), name='Prediction', legendgroup = '1',
                    #hovertemplate='%{y:.0f}'
                    ),
         go.Scatter(x=predictions_df_ar.index, y=predictions_df_ar['lower_bound'], mode='lines',
              marker=dict(size=1, color='rgba(0,0,0,0)', ), showlegend=False, name='95% CI', legendgroup = '1',
                    #hovertemplate='%{y:.0f}'
                    ),
         go.Scatter(x=predictions_df_ar.index, y=predictions_df_ar['upper_bound'], mode='lines',
               marker=dict(size=1, color='rgba(0,0,0,0)', ), fill='tonexty', opacity=0.1,
               fillcolor='rgba(204,255,153,0.3)', name='95% CI', legendgroup = '1',
                    hovertemplate='%{y:.0f}'
                    )
         ], rows=1, cols=1,
    )
    #fig.write_html('arima_plotly.html')
    #fig.show()

    #ETS PLOT
    #fig2 = go.Figure()
    fig.add_traces(
        [go.Scatter(x=data["Month"], y=data['total'], mode='lines+markers', marker=dict(size=10, color='white'),
                    name='Data', legendgroup = '2'),
         go.Scatter(x=df_fitted_ETS.index, y=df_fitted_ETS['fitted'], mode='lines',
                    marker=dict(size=10, color='lightblue' ), name='Fitted', legendgroup = '2'),
         go.Scatter(x=df_pred_ETS.index, y=df_pred_ETS.predicted, mode='lines+markers',
                    marker=dict(size=10, color='lightblue', symbol='triangle-right'), name='Prediction', legendgroup = '2'),
         go.Scatter(x=df_pred_ETS.index, y=df_pred_ETS['lower_bound'], mode='lines',
              marker=dict(size=1, color='rgba(0,0,0,0)', ), showlegend=False, name='95% CI', legendgroup = '2'),
         go.Scatter(x=df_pred_ETS.index, y=df_pred_ETS['upper_bound'], mode='lines',
               marker=dict(size=1, color='rgba(0,0,0,0)', ), fill='tonexty', opacity=0.1,
               fillcolor='rgba(153,255,255,0.3)', name='95% CI', legendgroup = '2')
         ], rows=2, cols=1
    )
    #fig2.write_html('ets_plotly.html')
    #fig2.show()

    #PROPHET PLOT
    #fig3 = go.Figure()
    fig.add_traces(
        [go.Scatter(x=data["Month"], y=data['total'], mode='lines+markers', marker=dict(size=10, color='white'),
                    name='Data', legendgroup = '3'),
         go.Scatter(x=df_fitted_pr.index, y=df_fitted_pr['fitted'], mode='lines',
                    marker=dict(size=10, color='yellow', ), name='Fitted', legendgroup = '3'),
         go.Scatter(x=df_predictions_pr.index, y=df_predictions_pr.predicted, mode='lines+markers',
                    marker=dict(size=10, color='yellow', symbol='triangle-right'), name='Prediction', legendgroup = '3'),
         go.Scatter(x=df_predictions_pr.index, y=df_predictions_pr['lower_bound'], mode='lines',
              marker=dict(size=1, color='rgba(0,0,0,0)', ), showlegend=False, name='95% CI', legendgroup = '3'),
         go.Scatter(x=df_predictions_pr.index, y=df_predictions_pr['upper_bound'], mode='lines',
               marker=dict(size=1, color='rgba(0,0,0,0)', ), fill='tonexty', opacity=0.1,
               fillcolor='rgba(255,255,153,0.3)', name='95% CI', legendgroup = '3')
         ], rows=3, cols=1,
    )
    #fig3.write_html('prophet_plotly.html')
    #fig3.show()

    fig.update_layout(autosize=False, height=1200, plot_bgcolor="#262730", legend_tracegroupgap=320)
    fig.update_xaxes(dtick="M3", tickangle=0, tickformat="%b\n%Y")
    fig.update_layout(hovermode="x unified")
    #fig.update_layout(calendar="gregorian")

    return fig

    '''#figs
    fig, ax = plt.subplots(3,1, figsize=(20, 28))
    #plt.style.use("dark_background")
    #plt.style.context(('dark_background'))
    #plt.figure(facecolor='#262730')
    #ax.set_facecolor('#262730')

    ax[0].grid(b=True, which='major', color='k', linestyle='-', alpha=0.5)
    ax[0].grid(b=True, which='minor', color='k', linestyle='-', alpha=0.1)
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax[0].xaxis.set_major_locator(mdates.YearLocator(1))
    ax[0].xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
    ax[0].xaxis.set_minor_locator(mdates.MonthLocator())

    ax[1].grid(b=True, which='major', color='k', linestyle='-', alpha=0.5)
    ax[1].grid(b=True, which='minor', color='k', linestyle='-', alpha=0.1)
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax[1].xaxis.set_major_locator(mdates.YearLocator(1))
    ax[1].xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
    ax[1].xaxis.set_minor_locator(mdates.MonthLocator())

    ax[2].grid(b=True, which='major', color='k', linestyle='-', alpha=0.5)
    ax[2].grid(b=True, which='minor', color='k', linestyle='-', alpha=0.1)
    ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax[2].xaxis.set_major_locator(mdates.YearLocator(1))
    ax[2].xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
    ax[2].xaxis.set_minor_locator(mdates.MonthLocator())


   ###PLOT 1
    sns.lineplot(x='Month', y='total', data=data, ax=ax[0], color='k', marker="o", markersize=10)
    sns.lineplot(x=predictions_df_ar.index, y=predictions_df_ar.predicted, data=predictions_df_ar, ax=ax[0], color='g', marker='>', markersize=10)
    sns.lineplot(x=fitted_df_ar.index, y=fitted_df_ar['fitted'],  data=fitted_df_ar, ax=ax[0], color='g')
    ax[0].fill_between(predictions_df_ar.index, predictions_df_ar['lower_bound'], predictions_df_ar['upper_bound'], alpha=0.2, facecolor='g')
    ax[0].set_title("Merchants Forecast for ARIMA", fontsize=25)
    ax[0].set_xlabel("Date", fontsize=15)
    ax[0].set_ylabel("Scaled Transactions", fontsize=15)
    ax[0].legend(loc="upper left", labels=['Data', 'Predictions', 'Fitted', 'Confidence Interval'], fontsize=15);

    ###PLOT 2
    sns.lineplot(x='Month', y='total', data=data, ax=ax[1], color='k', marker="o", markersize=10)
    sns.lineplot(x=df_pred_ETS.index, y=df_pred_ETS.predicted, data=df_pred_ETS, ax=ax[1], color='b', marker='>', markersize=10)
    sns.lineplot(x=df_fitted_ETS.index, y=df_fitted_ETS['fitted'], data=df_fitted_ETS, ax=ax[1], color='b')
    ax[1].fill_between(df_pred_ETS.index, df_pred_ETS['lower_bound'], df_pred_ETS['upper_bound'], alpha=0.2, facecolor='b')
    ax[1].set_title("Merchants Forecast for ETS", fontsize=25)
    ax[1].set_xlabel("Date", fontsize=15)
    ax[1].set_ylabel("Scaled Transactions", fontsize=15)
    ax[1].legend(loc="upper left", labels=['Data', 'Predictions', 'Fitted', 'Confidence Interval'], fontsize=15);
    ###PLOT 3
    sns.lineplot(x='Month', y='total', data=data, ax=ax[2], color='k', marker="o", markersize=10)
    sns.lineplot(x=df_predictions_pr.index, y=df_predictions_pr.predicted, data=df_predictions_pr, ax=ax[2], color='y', marker='>', markersize=10)
    sns.lineplot(x=df_fitted_pr.index, y=df_fitted_pr['fitted'], data=df_fitted_pr, ax=ax[2], color='y')
    ax[2].fill_between(df_predictions_pr.index, df_predictions_pr['lower_bound'], df_predictions_pr['upper_bound'], alpha=0.2, facecolor='y')
    ax[2].set_title("Merchants Forecast for Prophet", fontsize=25)
    ax[2].set_xlabel("Date", fontsize=15)
    ax[2].set_ylabel("Scaled Transactions", fontsize=15)
    ax[2].legend(loc="upper left", labels=['Data', 'Predictions', 'Fitted', 'Confidence Interval'], fontsize=15);


    fig.tight_layout()
    plt.show()
    plt.gcf()'''









    """data['Month'] = data['Month'].dt.strftime('%Y-%m')
    data = data.set_index('Month')
    data = data.rename_axis('timestamp')
    print(data.index)
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.format_xdata = mdates.DateFormatter('%Y-%m')
    df_fitted = df_fitted.reset_index()
    df_fitted['timestamp'] = df_fitted['timestamp'].dt.strftime('%Y-%m')
    df_fitted = df_fitted.set_index('timestamp')
    df_pred = df_pred.reset_index()
    df_pred['timestamp'] = df_pred['timestamp'].dt.strftime('%Y-%m')
    df_pred = df_pred.set_index('timestamp')
    ax.plot(data.index, data.total, marker="o", color='black', label='Total')
    ax.plot(df_pred.index, df_pred['predicted'], color='green', label='predicted',marker=">")
    ax.plot(df_fitted.index, df_fitted['fitted'], color='green', label='fitted')
    ax.fill_between(df_pred.index, df_pred['lower_bound'], df_pred['upper_bound'], alpha=0.2, facecolor='g')
    ax.set(title='Forecasts and simulations from Holt-Winters', xlabel='Year', ylabel='Scaled nº of Transactions')
    #monthly_locator = mdates.MonthLocator()

    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.format_xdata = mdates.DateFormatter('%Y-%m')
    ax.grid(True)
    #ax.grid(axis='x')
    #fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    plt.show()"""