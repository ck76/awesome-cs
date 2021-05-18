//阻塞
var fs = require("fs");

var data = fs.readFileSync('input.txt');

console.log(data.toString());
console.log("程序执行结束!");

//非阻塞
var fs = require("fs");

fs.readFile('input.txt', function (err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});

console.log("程序执行结束!");

//基于新版本 ES 的语法糖，Node 的异步操作可以替换成以下两种写法。
// 1、Promise

const _submit = (payload, formid, destination) => {
    return new Promise((resolve, reject) => { // 返回一个Promise对象，实现异步回调
        app.requestPost(destination, {
            payload,
            formid: formid
        }, true).then((res) => { // 调用一个异步函数，使用then方法对接成功回调
            if (res) {
                resolve(); // call成功回调
            } else {
                reject(); / call失败回调
            }
        }).catch(() => { // 调用一个异步函数，使用catch方法对接失败回调
            reject();
        })
    });
};
// 2、async/await

async function query(collection, querySelector, queryOptions) {
    let db, data;
    try {
        db = await MongoClient.connect(_dburl); // 使用await标记上游异步函数，此时event loop会将与该变量有关的操作阻塞
        data = await db.db(DBNAME).collection(collection).find(querySelector, queryOptions || {}).toArray();
    } catch (e) {
        log(e.message, 2);
    }
    return data;
}
