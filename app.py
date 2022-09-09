from turtle import width
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.write('oi tudo bem?')

st.write('tchau! Adeus!')

file = st.file_uploader('coloque um csv aqui')
if file:
    data = pd.read_csv(file)
    if st.checkbox('ver tabela'):
        n = st.number_input('coloque o número de linhas:',min_value=1,value = 5)
        col = st.multiselect('selecione as colunas',data.columns,default = list(data.columns))
        st.write(data.loc[0:n,col])
    if st.checkbox('Ver o Grafico'):
        graph_col = col = st.multiselect('selecione 2 colunas numericas',data.select_dtypes([int,float]).columns)
        if len(graph_col) == 2:
            coluna1 = graph_col[0]
            coluna2 = graph_col[1]
            fig,ax = plt.subplots()
            sns.scatterplot(x=coluna1,y=coluna2,data=data,ax=ax)
            st.pyplot(fig=fig)
            fig2 = px.scatter(data,x=coluna1,y=coluna2)
            st.plotly_chart(fig2)
    if st.checkbox('ver tableau'):
        html = "<div class='tableauPlaceholder' id='viz1662734024618' style='position: relative'><noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;La&#47;Lab_bi_analysis&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Lab_bi_analysis&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;La&#47;Lab_bi_analysis&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1662734024618');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
        st.components.v1.html(html,width = 2000,height = 2000)

