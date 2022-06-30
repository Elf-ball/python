#!/usr/bin/python
# -*- coding: utf-8 -*-

cd_weather = {
    "type": "object",
    "required": [
        "status",
        "count",
        "info",
        "infocode",
        "lives",
    ],
    "properties": {
        "status": {
            "type": "string"
        },
        "count": {
            "type": "string"
        },
        "info": {
            "type": "string"
        },
        "infocode": {
            "type": "string"
        },
        "lives": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "province",
                    "city",
                    "adcode",
                    "weather",
                    "temperature",
                    "winddirection",
                    "windpower",
                    "humidity",
                    "reporttime"
                ],
                "properties": {
                    "province": {
                        "type": "string"
                    },
                    "city": {
                        "type": "string"
                    },
                    "adcode": {
                        "type": "string"
                    },
                    "weather": {
                        "type": "string"
                    },
                    "temperature": {
                        "type": "string"
                    },
                    "winddirection": {
                        "type": "string"
                    },
                    "windpower": {
                        "type": "string"
                    },
                    "humidity": {
                        "type": "string"
                    },
                    "reporttime": {
                        "type": "string"
                    }
                }
            }
        }
    }
}
