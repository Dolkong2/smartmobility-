import streamlit as st
import numpy as np
import pandas as pd

st.title('동아대 한식 맛집!')
options = st.sidebar.selectbox("원하는 맛집을 고르시오", ["한식", "중식", "일식",'양식'])


if options == '한식':
        house = [' 누리마을 감자탕', '북창동 순두부', '쭈꾸미 도사', '수림 식당']
        review = [4.26,4.73,4.68,4.33]
        open = ['20240301','20100827','20160722 ','20180926']
        p_houses=pd.Series(house)
        p_reviews= pd.Series(review)
        p_opens=pd.Series(open)
        data = pd.DataFrame({'이름': p_houses,'리뷰': p_reviews,'최신순': p_opens})
        st.write(data)        
        

        option = st.selectbox(
        "평점,최신순,리뷰중 어떤걸 고르시겠습니까? ?",
        ('평점', "최신순"))
        

        if option == '평점':
                st.markdown("<p style='font-size:30px;'>평점", unsafe_allow_html=True)
                sorted_data = data.sort_values(by='리뷰', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)
                
                
                

        if option == '최신순':
                st.markdown("<p style='font-size:30px;'>최신순", unsafe_allow_html=True)  
                sorted_data = data.sort_values(by='최신순', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)

if options == '중식':
        house = [' 보배반점', '미담 짬뽕', '맘영궁', '홍콩반점']
        review = [4.43,4.99,4.11,4.26]
        open = ['20160322','20140724','20180630 ','20241122']
        p_houses=pd.Series(house)
        p_reviews= pd.Series(review)
        p_opens=pd.Series(open)
        data = pd.DataFrame({'이름': p_houses,'리뷰': p_reviews,'최신순': p_opens})
        st.write(data)        
        

        option = st.selectbox(
        "평점,최신순,리뷰중 어떤걸 고르시겠습니까? ?",
        ('평점', "최신순"))
        

        if option == '평점':
                st.markdown("<p style='font-size:30px;'>평점", unsafe_allow_html=True)
                sorted_data = data.sort_values(by='리뷰', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)
                
                
                

        if option == '최신순':
                st.markdown("<p style='font-size:30px;'>최신순", unsafe_allow_html=True)  
                sorted_data = data.sort_values(by='최신순', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)      

if options == '양식':
        house = ['봉대박 스파게티', '다맛', '홍카츠', '은하수 식당']
        review = [4.43,4.65,4.47,4.83]
        open = ['20150615','20130524','20191120 ','20191119']
        p_houses=pd.Series(house)
        p_reviews= pd.Series(review)
        p_opens=pd.Series(open)
        data = pd.DataFrame({'이름': p_houses,'리뷰': p_reviews,'최신순': p_opens})
        st.write(data)        
        

        option = st.selectbox(
        "평점,최신순,리뷰중 어떤걸 고르시겠습니까? ?",
        ('평점', "최신순"))
        

        if option == '평점':
                st.markdown("<p style='font-size:30px;'>평점", unsafe_allow_html=True)
                sorted_data = data.sort_values(by='리뷰', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)
                
                
                

        if option == '최신순':
                st.markdown("<p style='font-size:30px;'>최신순", unsafe_allow_html=True)  
                sorted_data = data.sort_values(by='최신순', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)  

if options == '일식':
        house = [' 시선', '다다하다', '온센', '야타이쇼부']
        review = [4.45,4.19,4.01,3.26]
        open = ['20100422','20121124','20121230 ','2012122']
        p_houses=pd.Series(house)
        p_reviews= pd.Series(review)
        p_opens=pd.Series(open)
        data = pd.DataFrame({'이름': p_houses,'리뷰': p_reviews,'최신순': p_opens})
        st.write(data)        
        

        option = st.selectbox(
        "평점,최신순,리뷰중 어떤걸 고르시겠습니까? ?",
        ('평점', "최신순"))
        

        if option == '평점':
                st.markdown("<p style='font-size:30px;'>평점", unsafe_allow_html=True)
                sorted_data = data.sort_values(by='리뷰', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)
                
                
                

        if option == '최신순':
                st.markdown("<p style='font-size:30px;'>최신순", unsafe_allow_html=True)  
                sorted_data = data.sort_values(by='최신순', ascending=False)
                sorted_names = sorted_data['이름']
                st.write(sorted_names)      
                    
                
                
        

        
                