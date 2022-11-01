const AWS = require('aws-sdk');


exports.handler = async (event) => {
    const s3 = new AWS.S3();
    const myBuckets = await s3.listBuckets().promise();
    
    console.log(myBuckets);
    
    
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};

