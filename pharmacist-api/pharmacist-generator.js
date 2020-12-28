/* eslint-disable no-async-promise-executor */
const nameGenerator = require('./name-generator.js');
const descGenerator = require('./desc-generator.js');

exports.generate = () => {
    let names = nameGenerator.generate(18);
    let descs = descGenerator.generate(18);

    let map = new Map();
    for (let i in names){
        map[names[i]]=descs[i];
    }

    return JSON.stringify(map); 
}
