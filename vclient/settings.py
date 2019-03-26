log_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '[%(filename)s - %(lineno)d] %(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },

    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },

        'FileHandler': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': './logs.log',
            'class': 'logging.FileHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'FileHandler'],
            'level': 'DEBUG',
        },

        'pika': {
            'level': 'CRITICAL',
        },


        'urllib3.connectionpool': {
            'level': 'CRITICAL'
        }
    }
}

SERVER_IP = '212.109.195.39'
SERVER_PORT = 5672
