import streamlit as st

st.set_page_config(
    page_title= '준호홈',
    page_icon = '😁'
)

menu = st.sidebar.selectbox('MENU', ['자기소개','학교소개','동아리소개','관심분야','디지털 교과서'])
if menu == '자기소개':
    st.subheader('자기소개🤑')
    st.title('이준호')
    st.subheader('생일')
    st.subheader('2006년02월23년')
    st.subheader('취미')
    st.subheader('운동을 좋아함')
    col3, col4 = st.columns(2)
    with col3:
        image1 = ('soccer.jpg')
        st.image(image1,width=300)
    with col4:
        image2 = ("basketball.jpg")
        st.image(image2,width=300)
    st.subheader('장래희망')
    st.subheader('앱 개발 프로그래머')

elif menu == '학교소개':
    st.subheader('학교소개')

    col1, col2 = st.columns(2)
    with col1:
        st.header('강북고등학교')
        st.subheader('일반계 고등학교')

        st.write('대구광역시 북구 태전로 100에 위치한 사립 일반계 고등학교이다. 1974년 2차 인문계 고등학교인 "배영고등학교"로 개교하여 1997년 교명을 "강북고등학교"로 개명하며 일반 인문계 고등학교로 격상되었다.')
        st.subheader('교훈')
        st.subheader('"꿈을 지닌 사람, 능력있는 사람, 도덕적인 사람"')
        st.subheader('설립_1974 ~ 현재')
        st.subheader('사립')
        st.subheader('교장:박종창')
        image3 = ('principal.jpg')
        st.subheader('교가')
        st.video('https://youtu.be/CMNhMd27KqU')

        st.image(image3,width=300)
        st.subheader('홈페이지')
        st.caption('https://gangbuk.dge.hs.kr/gangbukh/main.do?sysId=gangbukh')
    with col2:
        image = ('schools1.jpg')
        st.image(image, width=500)






elif menu == '동아리소개':
    st.subheader('동아리소개😳')
    st.title('정보 기술 심화탐구')
    st.subheader('게임 개발')
    image10=('unity.png')
    st.image(image10,width=300)
    image11=('game.png')
    st.image(image11,width=500)



elif menu == '관심분야':
    st.subheader('관심분야')
    st.title('앱 개발자')
    col5,col6 = st.columns(2)
    with col5:
        st.image('1234.png',width=300)
    with col6:
        st.image('111.jpg',width=300)

    st.caption('https://namu.wiki/w/%EA%B0%9C%EB%B0%9C%EC%9E%90')
    st.video('https://www.youtube.com/watch?v=MvD6_eor0Kg')
    st.header('게임')
    col10,col12,col11=st.columns(3)
    with col10:
        st.subheader('FPS')
    with col12:
        st.subheader('VS')
    with col11:
        st.subheader('RPG')
    col7,col8,col9= st.columns(3)
    with col7:
        image7=('sudden.jpg')
        st.image(image7)
    with col8:
        image8 = ('ground.jpg')
        st.image(image8)
    with col9:
        image9 = ('story.jpg')
        st.image(image9)


elif menu == '디지털 교과서':

      genre = st.radio(
          "생명과학",
          ['3과','4과']
      )
      if genre =="3과":
          st.header('생명과학')
          st.subheader('신경계')
          st.write('뉴런')
          image15=('뉴런.png')
          st.image(image15)
          st.write('흥분전도')
          image16=('흥분전도.png')
          st.image(image16)
          st.write('근수축')
          image17=('근수축.png')
          st.image(image17)
          st.write('뇌')
          image18=('shl.png')
          st.image(image18)

      elif genre =='4과':
          st.header('생명과학')
          st.subheader('유전')
          st.write('체새포 분열')
          image12=('qwer.jpg')
          st.image(image12)
          st.write('생식세포 분열')
          image13=('asdf.jpg')
          st.image(image13)
          st.write('DNA상대량')
          image14=('zxcv.jpg')
          st.image(image14,width=600)






