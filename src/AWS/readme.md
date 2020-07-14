# AWS service trial

```

```

Go to aws page and get key

```
aws configure
```

put, key, secret key, ap-northeast-1

## create SSH key

- set AWS keys from web site
- setting up cdk

```
ckd bootstrap
```

go to [here](https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks?filteringText=&filteringStatus=active&viewNested=true&hideStacks=false&stackId=arn%3Aaws%3Acloudformation%3Aap-northeast-1%3A050138915699%3Astack%2FMyFirstEc2%2Febb7ddb0-c5cb-11ea-895f-0ac3b391d020) to delete invalid stack.


- Just execute following code **once**.

```
export KEY_NAME="NewHirakeGoma"
aws ec2 create-key-pair --key-name ${KEY_NAME} --query 'KeyMaterial' --output text > ${KEY_NAME}.pem
mv NewHirakeGoma.pem ~/.ssh/
chmod 400 ~/.ssh/NewHirakeGoma.pem
cdk deploy -c key_name="NewHirakeGoma"
```

> Outputs:
MyFirstEc2.InstancePublicIp = 54.95.98.35
MyFirstEc2.InstancePublicDnsName = ec2-54-95-98-35.ap-northeast-1.compute.amazonaws.com
> 
> Stack ARN:
arn:aws:cloudformation:ap-northeast-1:050138915699:stack/MyFirstEc2/571a6e30-c5d4-11ea-895f-0ac3b391d020


```
ssh -i ~/.ssh/NewHirakeGoma.pem ec2-user@54.95.98.35
```

<details>
<summary>
ERROR like "Invalid Key~" Occurred ?
</summary>
- Invalid Keyとなる理由は簡単だった
- `aws ec2 create-key-pair --key-name ${KEY_NAME} --query 'KeyMaterial' --output text > ${KEY_NAME}.pem` このコマンドを複数回うったのが原因
- 一度作ったキーペアを消すのは面倒？

まちがって作ったので別の名前で作ることにした。
- Another key patttern In doc2
</details>




<details>
<summary>
SS3.5 "hands on" TEST code
</summary>
```
bucketName="mybucket-$(openssl rand -hex 12)"
echo $bucketName
aws s3 mb "s3://${bucketName}"
```

> make_bucket: mybucket-b6fbf7f5f41a6bb0bb9080ef

`aws s3 ls`


```
echo "Hello world!" > hello_world.txt
aws s3 cp hello_world.txt "s3://${bucketName}/hello_world.txt"
```

- delete bucket

```
aws s3 rb "s3://${bucketName}" --force
```

</details>

