#!/bin/bash
echo "Exporting GOPATH to $(pwd)"
export GOPATH=$GOPATH:$(pwd)
# TODO FIX no install location for directory /opt/app/cmd/sefeed outside GOPATH
echo "Installing dependencies..."
go get ./...
echo "Building app..."
go build cmd/sefeed/sefeed.go
echo "Runinng Super-Express Feed..."
./sefeed
