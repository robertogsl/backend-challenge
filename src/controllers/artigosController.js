const artigosModel = require('../models/artigosModel') 

const getAll = async (_req, res) => {
    const artigos = await artigosModel.getAll();
    return res.status(200).json(artigos);
}

const categoryFilter = async (req, res) => {
    const { category } = req.params;

    const artigos = await artigosModel.categoryFilter(category);
    return res.status(200).json(artigos);
}

const titleFilter = async (req, res) => {
    const { title } = req.params;

    const artigos = await artigosModel.titleFilter(title);
    return res.status(200).json(artigos);
}

module.exports = {
    getAll,
    categoryFilter,
    titleFilter
};