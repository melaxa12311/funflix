const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Backend running successfully 🚀");
});

app.listen(4000, () => {
  console.log("Backend running on port 4000");
});

