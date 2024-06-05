


def bmi_range(bmi):
   if(bmi<=10):
       st.info('저체중입니다.') 
   elif(10<=bmi<=23):
       st.warning('정상입니다.')
   else:
       st.error('과체중입니다.') 
