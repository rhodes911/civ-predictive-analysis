#!/usr/bin/env python3
"""
Simple status server for dashboard connection indicator
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from datetime import datetime

class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Read current status
            status = self.get_live_status()
            self.wfile.write(json.dumps(status).encode())
        
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Civ VI Live Connection Status</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .connected { color: green; }
                    .disconnected { color: red; }
                    .status-box { 
                        border: 1px solid #ccc; 
                        padding: 20px; 
                        border-radius: 5px; 
                        margin: 20px 0;
                        background: #f9f9f9;
                    }
                </style>
                <script>
                    function updateStatus() {
                        fetch('/status')
                            .then(response => response.json())
                            .then(data => {
                                document.getElementById('status').innerHTML = 
                                    data.connected ? 
                                    '<span class="connected">🟢 CONNECTED</span>' : 
                                    '<span class="disconnected">🔴 DISCONNECTED</span>';
                                document.getElementById('message').textContent = data.message;
                                document.getElementById('last_turn').textContent = data.last_turn;
                                document.getElementById('timestamp').textContent = 
                                    new Date(data.timestamp * 1000).toLocaleString();
                            })
                            .catch(err => {
                                document.getElementById('status').innerHTML = 
                                    '<span class="disconnected">🔴 ERROR</span>';
                                document.getElementById('message').textContent = 'Failed to fetch status';
                            });
                    }
                    
                    setInterval(updateStatus, 2000);
                    updateStatus();
                </script>
            </head>
            <body>
                <h1>🎮 Civ VI Live Connection Status</h1>
                <div class="status-box">
                    <h2>Connection: <span id="status">⏳ Loading...</span></h2>
                    <p><strong>Message:</strong> <span id="message">-</span></p>
                    <p><strong>Last Turn:</strong> <span id="last_turn">-</span></p>
                    <p><strong>Last Update:</strong> <span id="timestamp">-</span></p>
                </div>
                
                <h3>📋 Setup Instructions:</h3>
                <ol>
                    <li>Install the Civ VI Live Data Exporter mod</li>
                    <li>Start a Civ VI game</li>
                    <li>Run: <code>live_monitor.bat start</code></li>
                    <li>Watch this page for live updates</li>
                </ol>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        
        else:
            self.send_response(404)
            self.end_headers()
    
    def get_live_status(self):
        try:
            # Try dashboard status first
            if os.path.exists('live_data/dashboard_status.json'):
                with open('live_data/dashboard_status.json', 'r') as f:
                    return json.load(f)
            
            # Fall back to connection status
            if os.path.exists('live_data/connection_status.json'):
                with open('live_data/connection_status.json', 'r') as f:
                    return json.load(f)
                    
        except Exception as e:
            pass
        
        return {
            'connected': False,
            'message': 'No status file found - mod not running',
            'timestamp': 0,
            'last_turn': -1
        }

def main():
    server = HTTPServer(('localhost', 8089), StatusHandler)
    print("🌐 Status server running at http://localhost:8089")
    print("📊 Dashboard integration available")
    print("🔗 Connection status API: http://localhost:8089/status")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Status server stopped")

if __name__ == '__main__':
    main()
