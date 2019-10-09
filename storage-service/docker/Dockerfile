FROM openjdk:8
COPY ./target/app.jar /root/project/
WORKDIR /root/project
ENTRYPOINT ["java","-Dspring.profiles.active=${PROFILE}","-jar","app.jar"]
