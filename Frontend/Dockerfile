# ---------- Build stage ----------
FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

# Pass API URL at build time
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# For Vite, use VITE_API_URL instead:
# ARG VITE_API_URL
# ENV VITE_API_URL=$VITE_API_URL

RUN npm run build

# ---------- Production stage ----------
FROM nginx:alpine

# For Create React App, build output is /app/build
# COPY --from=build /app/build /usr/share/nginx/html

# For Vite, build output is /app/dist – comment the line above and uncomment:
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]