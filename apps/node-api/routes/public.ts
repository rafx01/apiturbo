import express from "express";

const router = express.Router();

router.post("/add-user", (req, res) => {
  const response = req.body;

  res.status(201).json(response);
});

router.get("/get-all-users", (req, res) => {});

router.put("/edit-user/:userId", (req, res) => {
  const user = req.headers;
});

export default router;
