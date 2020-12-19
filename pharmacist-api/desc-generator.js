const fs = require('fs');

const CHAIN_PATH = 'desc-chain.json';

exports.generate = (total) => {
    let chainData = fs.readFileSync(CHAIN_PATH);
    let chain = JSON.parse(chainData);

    const nextWord = (currentWord, chain) => {
        if (currentWord.endsWith('.')) return currentWord; //base case

        const sum = (a, b) => parseInt(a) + parseInt(b);
        const vals = (obj) => Object.values(obj);

        let countSum = vals(vals(chain[currentWord])).reduce(sum);
        let randSum = Math.random() * countSum;

        let shuffleKeys = Object.keys(chain[currentWord]);
        // eslint-disable-next-line no-unused-vars
        shuffleKeys.sort((a, b) => Math.random() - 0.5);


        let newCurrent;
        for (let key of shuffleKeys) {
            randSum -= chain[currentWord][key];
            if (randSum < 0) {
                newCurrent = key;
            }
        }
        return currentWord + ' ' + nextWord(newCurrent, chain);
    }

    let descriptions = [total];
    for (let i = 0; i < total; i++) {
        let desc = nextWord('used', chain);
        //capitalizing first letter:
        descriptions[i] = (desc.charAt(0).toUpperCase() + desc.slice(1)).replace('(', '').replace(')', '')
    }
    return descriptions;
}