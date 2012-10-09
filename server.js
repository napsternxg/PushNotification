var app = require('http').createServer(handler),
io = require('socket.io').listen(app),
fs = require('fs');

app.listen(8000)

function handler(req, res){
	fs.readFile( __dirname + '/client.html' ,
		function(err, data){
			if(err){
				console.log(err);
				res.writeHead(500);
				return res.end("Error outputing the data");
			}
			res.writeHead(200);
			res.end(data);
	});
}

io.sockets.on('connection', function(socket){
	fs.watch('response.json', function(curr, prev){
		fs.readFile('response.json', 'utf8', function(err, data){
			if(err) throw err;
			console.log(data);
			data = JSON.parse(data);
			data.time = new Date();
			
			socket.volatile.emit('notification', data);
		});
		
	});
});