const http = require('http');
const port = process.env.PORT || 3000;
const version = process.env.VERSION || unknowversion;
const hostnamesvr = process.env.HOSTNAME || unknowhostname;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  const msg = `Hello World NodeJS ${version} ${hostnamesvr}!\n`
  res.end(msg);
});

server.listen(port, () => {
  console.log(`Server running on http://localhost:${port}/`);
});
