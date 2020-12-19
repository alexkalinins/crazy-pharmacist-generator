const fs = require('fs');

const CHAIN_PATH = 'name-chain.json';

const MIN_LENGTH = 6;
const MAX_LENGTH = 9;

exports.generate = (total) => {
    let chainData = fs.readFileSync(CHAIN_PATH);
    let chain = JSON.parse(chainData);

    // todo assumes we good now with chain

    const pickChar = (probs) => {
        const sum = (total, num) => parseInt(total) + parseInt(num);

        // keys are shuffled
        let shuffleKeys = Object.keys(probs);
        // eslint-disable-next-line no-unused-vars
        shuffleKeys.sort((a, b) => Math.random() - 0.5);

        // let probSum = probs.values().reduce(sum);
        let probSum = Object.values(probs).reduce(sum);
        let randomSum = Math.random() * probSum;

        for (let key of shuffleKeys) {
            randomSum -= probs[key];
            if (randomSum < 0) {
                return key;
            }
        }
        return shuffleKeys[0] // would never run but just in case

    }

    const isVowel = (aChar) => {
        return aChar == 'a' ||
            aChar == 'e' ||
            aChar == 'o' ||
            aChar == 'u' ||
            aChar == 'i' ||
            aChar == 'y' ||
            // dot is not vowel but prevents ugly endings like 'ae'
            aChar == '.' ||
            // also not a vowel but prevents ugly starts like 'ae'
            aChar == '';
    }

    const nextChar = (prevChar, currChar, chain) => {
        if (currChar == '.') return ''; //base case

        let picked;
        let pastAreVowel = isVowel(prevChar) && isVowel(currChar);
        let pastAreConson = !isVowel(prevChar) && !isVowel(currChar);

        do {
            picked = pickChar(chain[currChar]);
            // preventing three vowels/consonants in a row.
        } while ((pastAreVowel && isVowel(picked)) || (pastAreConson && !isVowel(picked)));

        return currChar + nextChar(currChar, picked, chain); // recursive case
    }

    const makeWord = (chain) => {
        let firstChar = pickChar(chain['_first']);
        return nextChar('', firstChar, chain);
    }

    const isSpunky = (word) => {
        return word.includes('z') ||
            word.includes('q') ||
            word.includes('x') ||
            word.includes('j') ||
            word.includes('r');
    }

    const generateGoodWord = (chain) => {
        let word;
        do {
            word = makeWord(chain);
        } while (word.length < MIN_LENGTH || word.length > MAX_LENGTH || !isSpunky(word));

        return word;
    }


    //  this is where the magic happens
    let words = [total];
    for (let i = 0; i < total; i++) {
        let word = generateGoodWord(chain);
        words[i] = word.charAt(0).toUpperCase() + word.slice(1);
    }

    return words;

}