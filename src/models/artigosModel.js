const connection = require('./connection')

const getAll = async () => {
    const [artigos] = await connection.execute("SELECT * FROM artigos ORDER BY date DESC");
    return artigos;
};

const categoryFilter = async (category) => {
    const [artigos] = await connection.execute(`SELECT * FROM artigos WHERE category = "${category}"`);
    return artigos;
};

const titleFilter = async (title) => {
    const [artigos] = await connection.execute(`SELECT * FROM artigos WHERE title LIKE '%${title}%'`);
    return artigos;
};

module.exports = {
    getAll,
    categoryFilter,
    titleFilter
};