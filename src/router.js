const express = require('express');
const artigosController = require('./controllers/artigosController')

const router = express.Router();

router.get('/artigos', artigosController.getAll);

router.get('/artigos/:category', artigosController.categoryFilter);

router.get('/artigos/title/:title', artigosController.titleFilter);

module.exports = router;