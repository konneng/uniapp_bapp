
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import admin from "firebase-admin";
import { Pool } from "pg";
import authRoutes from "./routes/auth.js";
import userRoutes from "./routes/users.js";
import deviceRoutes from "./routes/devices.js";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

admin.initializeApp({
  credential: admin.credential.cert(JSON.parse(process.env.FIREBASE_SERVICE_ACCOUNT))
});

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

app.use((req, res, next) => {
  req.db = pool;
  next();
});

app.use("/auth", authRoutes);
app.use("/users", userRoutes);
app.use("/devices", deviceRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`API listening on port ${PORT}`));
