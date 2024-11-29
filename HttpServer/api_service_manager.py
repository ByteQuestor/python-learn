#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：HttpServer 
@File    ：api_service_manager.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/29 10:18 
'''
import http.server
import socketserver


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request for path: {self.path}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"GET request received and processed successfully!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received POST request for path: {self.path} with data: {post_data.decode('utf-8')}")
        self.send_response(201)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"POST request received and processed successfully!")

    def do_DELETE(self):
        print(f"Received DELETE request for path: {self.path}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"DELETE request received and processed successfully!")


if __name__ == "__main__":
    PORT = 8080
    Handler = MyRequestHandler

    with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
        print(f"Server started on port {PORT}")
        httpd.serve_continue()
