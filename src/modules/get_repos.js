/* API
 * A api for my projects and other things
 * Github: https://www.github.com/awesomelewis2007/api
 * By: Lewis Evans
*/

const axios = require('axios');
const fs = require('fs');
const path = require('path');

const getRepos = async () => {
    const { data } = await axios.get('https://api.github.com/users/awesomelewis2007/repos');
    const repos = data.filter(repo => !repo.fork).map(repo => repo.name);
    console.log(repos);
}

getRepos();