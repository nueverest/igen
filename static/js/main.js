// document.addEventListener('DOMContentLoaded', function() {

//     // 选择所有的提示按钮并为它们添加点击事件监听器
//     document.querySelectorAll('.prompt-button').forEach(button => {
//         button.addEventListener('click', function(event) {
//             event.preventDefault();  // 防止表单默认提交行为
//             let userInput = this.getAttribute('data-prompt');  // 获取 data-prompt 属性作为用户输入
//             fetch('/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/x-www-form-urlencoded',
//                 },
//                 body: `user_input=${encodeURIComponent(userInput)}`
//             })
//             .then(response => response.json())
//             .then(data => {
//                 // 处理响应数据，即显示图像
//                 const imagesContainer = document.getElementById('imagesContainer');
//                 imagesContainer.innerHTML = '';  // 清除之前的图像
//                 console.log(222);
//                 data.images.forEach(imageUrl => {
//                     let imgElement = document.createElement('img');
//                     imgElement.src = imageUrl;
//                     imagesContainer.appendChild(imgElement);
//                 });
//             })
//             .catch(error => console.log('Error:', error));
//         });
//     });
// });


// Function to save the generated image

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.prompt-button').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // 防止默认的表单提交
            let userInput = this.getAttribute('data-prompt');
            document.getElementById('userInput').value = userInput; // 设置隐藏字段的值
            document.getElementById('promptForm').submit(); // 提交表单
        });
    });
});


function saveImage(imageId) {
    var image = document.getElementById(imageId);  // 获取图片元素
    var imageUrl = image.src;  // 获取图片的 URL
    var link = document.createElement('a');  // 创建一个<a>元素用于下载
    link.href = imageUrl;  // 设置下载链接
    link.download = 'DownloadedImage.png';  // 设置下载的文件名
    document.body.appendChild(link);  // 将<a>元素添加到文档
    link.click();  // 模拟点击<a>元素
    document.body.removeChild(link);  // 删除<a>元素
}