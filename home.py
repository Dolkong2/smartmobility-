import streamlit as st

def bmi_range(bmi):
   if(bmi<=10):
       st.info('저체중입니다.') 
   elif(10<=bmi<=23):
       st.warning('정상입니다.')
   else:
       st.error('과체중입니다.') 



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
    bmi_range(bmi)
      



 

