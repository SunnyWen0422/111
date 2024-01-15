// index.js  
  
// 引入必要的模块  
const mysql = require('mysql');  
  
// 创建与数据库的连接  
const connection = mysql.createConnection({  
  host: 'localhost', // 数据库主机地址  
  user: 'root', // 数据库用户名  
  password: 'Sunny418', // 数据库密码  
  database: 'menu' // 数据库名称 
});  
  
Page({  
  data: {  
    result: ''  
  },  
  
  // calculate函数，从数据库中调取数据  
  calculate() {  
    // 在这里添加查询数据的逻辑  
    connection.query('SELECT * FROM your_table', (error, results, fields) => {  
      if (error) throw error;  
      // 将查询结果赋值给result，以便在页面上显示  
      this.setData({  
        result: JSON.stringify(results)  
      });  
    });  
  },   
});