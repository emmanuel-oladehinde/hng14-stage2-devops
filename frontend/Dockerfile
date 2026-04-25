FROM node:18-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install

FROM node:18-slim
WORKDIR /app
RUN useradd -m hnguser && chown hnguser:hnguser /app
USER hnguser
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=hnguser:hnguser . .
EXPOSE 3000
CMD ["node", "app.js"]
