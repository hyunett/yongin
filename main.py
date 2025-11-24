import streamlit as st

st.title("나의 첫 웹서비스!!")
name = st.text_input("이름을 입력해주세요.")
menu = st.selectbox('가장 많이 쓰는 앱은?', ['인스타그램', '페이스북', '트위터', '유튜브'])
time = st.slider('하루 사용 시간은? ', 0, 24, 3)


def awareness_message(hours: int) -> str:
    """시간 사용량 구간별 경각심 문구를 반환."""
    if hours < 3:
        return "지금처럼 짧게 사용하는 패턴을 유지하면 다른 생활 리듬도 더 탄탄해져요."
    if hours < 6:
        return "살짝 늘어난 사용시간입니다. 예비 알람을 걸어두고 쉬는 시간을 꼭 챙겨보세요."
    if hours < 9:
        return "업무·학습 시간을 침범하기 직전이에요. 1시간마다 눈 건강 체크를 해보면 어떨까요?"
    if hours < 12:
        return "하루 절반 가까이를 화면 앞에서 보내고 있어요. 대면 활동을 계획해 균형을 맞춰주세요."
    if hours < 15:
        return "12시간을 넘으면 수면·운동 시간이 급격히 줄어듭니다. 강제 로그아웃 규칙을 세워보세요."
    if hours < 18:
        return "18시간 이상은 위험 신호예요. 기기 사용 이유부터 다시 점검하고 도움을 구할 때입니다."
    if hours < 21:
        return "24시간 중 대부분을 앱에 쓰고 있어요. 건강과 인간관계에 치명적일 수 있어 긴급 조정이 필요합니다."
    return "거의 하루 종일 연결된 상태입니다. 전문가 상담을 포함한 강력한 디지털 디톡스를 즉시 고려하세요."

if st.button('결과 보기'):
    st.write(f'{name}님은 {menu}를 하루 평균 {time}시간 사용하시네요. 균형 잡힌 시간관리가 중요해요!')
    st.write(awareness_message(time))
    st.balloons()
