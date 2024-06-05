import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import myfunc as my 

st.session_state.id = '서석빈'
st.write(st.session_state.id,'님 반갑습니다.')

selected = st.sidebar.selectbox('목차',('체질량 계산기','갭마인더','국가별 통계')) # sidebar와 selected box 확인해보기

if selected == '체질량 계산기':


   st.title('체질량 지수 계산기') #제목
   st.info('체질량 지수는 자신의 몸무게를 키의 제곱으로 나누 값입니다.') # 글자에 형광펜 같이 색깔을 넣을때
   height=st.number_input('신장(cm)',value=160, step=3 )
   st.write("당신의 신장은: ",height,'cm')

   weight=st.number_input('몸무게(kg)',value=60, step=1 )
   st.write("당신의 몸무게는:", weight, 'cm')

   if st.button('계산하기'):
       st.image('original.jpg', caption='flowers by the mountains') # image 
    
    
    
       bmi=weight/((height/100)**2)
       st.write(f'당신의 체지방 지수는 {round(bmi)} 입니다.')
       my. bmi_range(bmi)
if selected == '갭마인더':
    st.title('갭마인더')
    st.write('파일 불러오기')
    data = pd.read_csv('gapminder.csv')
    year=st.slider('Select a Year',1952,2007,1952,step=5) #slider 찾아보기
    st.write(f'{year}년도')
    
    data = data[data['year']==year]
    st.write(data)
    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s = data['pop']*0.000002) # x, y 좌표로 되게 한다.
    st.pyplot(fig)
    colors=[]
    for x in data['continent']:
        if x=='Africa':
            colors.append('royalblue')
        elif x=='Americas':
            colors.append('green')
        elif x=='Asia':
            colors.append('tomato')
        elif x=='Europe':
            colors.append('orange') 
        else:
            colors.append('purple')
    plt.scatter(data['gdpPercap'])
    plt.title('GDP per capital and Life Expctancy in 2007')
    plt.xlabel('GDP per Capital')
    plt.ylabel('Life Expectancy')
    plt.show()                      



  
    

if selected == ('국가별 통계'):
    st.title('국가별 통계') 
    df=pd.read_csv('gapminder.csv')     
    #st.write(df)
    
    country = df['country'].unique()
    #st.write(country)
    
    options = st.multiselect(
    "국가를 선택 하세요.",
    country,
    ['Korea, Rep.']
    )

    st.write("You selected:", options[0])
    #x = options[0]
    #st.write(df[df['country'] ==x ])
    fig, ax = plt.subplots()
    for x in options:
        ax.plot(df[df['country'] ==x ]['year'],df[df['country'] ==x ]['gdpPercap'])
    st.pyplot(fig)

    fig1,ax1= plt.subplots()
    for x in options:
        ax1.plot(range(len(df[df['country']==x]['lifeExp'])),df[df['country'] == x]['lifeExp'],label = x)
    ax1.legend()
    ax1.set_xticks(range(len(df [df['country']==x]['pop'])),df[df['country'] ==x]['year'])
    ax1.set_title('Life Expectancy')
    st.pyplot(fig1)

    df2007 = df[df['year'] ==2007]
    df2007.reset_index(drop = True,inplace=True)
    colors=[]
 

