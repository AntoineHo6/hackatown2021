# Stage 0, build and compile react app
FROM tiangolo/node-frontend as build-stage

WORKDIR /app

COPY ./package*.json /app/
RUN npm install

COPY ./ /app/
RUN npm run build

# Stage 1, nginx to serve compiled web app
FROM nginx

COPY --from=build-stage /app/build/ /usr/share/nginx/html

# Copy default nginx.conf from tiangolo/node-frontend
COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
