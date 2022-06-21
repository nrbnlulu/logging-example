import logging
from logging.config import dictConfig

LOG_CONFIG = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'std',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
          'detailed_console': {
            'level': 'DEBUG',
            'formatter': 'error',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'std_fh': {
            'level': 'INFO',
            'formatter': 'std',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/std.log',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        },
        'detailed_fh': {
            'level': 'WARNING',
            'formatter': 'error',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/errors.log',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        }
    },
    'loggers': {
        '': {  # root logger
            'level':'NOTSET',
            'handlers': ['std_fh', 'console'],
            
        },
        'D.src': {
            'propagate': False,
            'handlers': ['detailed_fh','detailed_console'],
          
        },
         'src': {
            'propagate': False,
            'handlers': ['std_fh','console'],
          
        }
    },
    'formatters': {
        'std': {
            'format': '[%(levelname)s  - %(asctime)s - %(name)s::] %(message)s'
        },
        'error': {
            'format': '[%(levelname)s - %(asctime)s - %(name)s - %(process)d::module :%(module)s|Line: %(lineno)s]  messages:[ %(message)s ]'
        },

    }
}

logging.config.dictConfig(LOG_CONFIG)
rootL = logging.getLogger() # this is a root logger
srcL = logging.getLogger(__name__) # this is an `src` logger 
detL = logging.getLogger("D.") # this is 'detailed' 

def main():
    rootL.debug("hello from rootL")
    srcL.debug("hello from srcL")
    detL.debug("hello from detL")
    srcL.warning("fdsafds")
    import animals.cat
    import animals.cow
    import animals.fish
    
if __name__ == '__main__':
    main()