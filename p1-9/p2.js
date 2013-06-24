var sum = 0;
lastNum = 1;
num = 1;
while(num <= 4000000) {
	if (num % 2 === 0) {
		sum += num;
	}
	var temp = num;
	num = lastNum + num;
	lastNum = temp;
	console.log('Bsum=',sum,' lastNum=',lastNum, ' num=',num);
}
console.log(sum);