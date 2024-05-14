#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <bit.ly URL>"
  exit 1
fi

bitly_url="$1"

# Use curl to get the headers and find the Location header
real_url=$(curl -sI "$bitly_url" | grep -i '^location:' | cut -d ' ' -f2- | tr -d '\r')

if [ -n "$real_url" ]; then
  echo "The real address is: $real_url"
else
  echo "Unable to resolve the bit.ly URL."
fi
