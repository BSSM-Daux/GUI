import streamlit as st
import yaml
import time
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose

st.set_page_config(layout="wide")

with open("position.yaml", "r") as file:
    data = yaml.safe_load(file)

# Initialize ROS context if it's not already initialized
if not rclpy.ok():
    rclpy.init()

def same_position():
    pass

def move_to_goal():
    pass

def button_clicked(key, args=None):
    x, y, z = data[key].values()
    x = float(x.strip().replace(',', ''))
    y = float(y.strip().replace(',', ''))
    z = float(z)

    print(type(x), type(y), type(z))
    print(x, y, z)

    node = rclpy.create_node('move_to_goal')

    goal_publisher = node.create_publisher(PoseStamped, '/goal_pose', 10)

    # 원하는 위치로 이동하기 위한 목표 좌표 설정
    goal_pose = PoseStamped()
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.position.z = z
    goal_pose.pose.orientation.w = 1.0  # 기본 방향으로 설정

    while goal_publisher.get_subscription_count() < 1:
        rclpy.spin_once(node)

    # 목표 좌표를 게시하여 로봇을 이동시킴
    goal_publisher.publish(goal_pose)

    node.destroy_node()

def main():
    st.markdown("""
    <h1 style='text-align: center; color: black;'>이동할 경로를 클릭해주세요.</h1><br><br><br><br>
    """, unsafe_allow_html=True)

    columns_1 = st.columns((3, 3, 3, 3))
    columns_2 = st.columns((1, 10, 1))  # layer 크기 지정


    with columns_1[0]:
        if st.button("임베디드 사무실로 이동하기", key="embedlab", use_container_width=True):
            button_clicked("embedlab")
        if st.button("SW개발실 3으로 이동하기", key="class3", use_container_width=True):
            button_clicked("class3")

    with columns_1[1]:
        if st.button("헬스장으로 이동하기", key="gym", use_container_width=True):
            button_clicked("gym")
        if st.button("SW개발실 2으로 이동하기", key="class2", use_container_width=True):
            button_clicked("class2")

    with columns_1[2]:
        if st.button("작은 발표장으로 이동하기", key="smallpresroom", use_container_width=True):
            button_clicked("smallpresroom")
        if st.button("SW개발실 1으로 이동하기", key="class1", use_container_width=True):
            button_clicked("class1")

    with columns_1[3]:
        if st.button("도서관으로 이동하기", key="library", use_container_width=True):
            button_clicked("library")
        if st.button("화장실로 이동하기", key="toilet", use_container_width=True):
            button_clicked("toilet")

    st.write("")

    with columns_2[1]:
        value = "이동합니다."
        st.markdown(f"""
           <h4 style='text-align: center; color: black;'><br><br><br><br>{value}</h4>
           """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
