FROM alpine:3.14
RUN apk add --update nodejs npm
RUN apk add py3-pip
WORKDIR /app
COPY . /app
COPY package*.json ./
RUN pip3 install -r requirements.txt
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node","server.js"]
