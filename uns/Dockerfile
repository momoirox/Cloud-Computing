FROM openjdk:19

EXPOSE 8080

ARG JAR_FILE= ./*.jar

COPY ./uns.jar uns.jar

ENTRYPOINT ["java","-jar","/uns.jar" ]
