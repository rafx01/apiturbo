import express from "express";
import publicRoutes from "./routes/public";

const app = express();
app.use(express.json);

app.use("/", publicRoutes);

app.listen(4000, () => {
  console.log("API rodando na porta 4000");
});
