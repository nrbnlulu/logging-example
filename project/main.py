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
          'my_detailed_console': {
            'level': 'WARNING',
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
        'my_detailed_fh': {
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
        '': {  # root logger, all other loggers will be of this logger level implicitlly.
            'level':'DEBUG',
            'handlers': ['std_fh', 'console'], 
            
        },
        'my_detailed': {
            'level': 'WARNING',
            'propagate': False,
            'handlers': ['my_detailed_fh','my_detailed_console'],
          
        },
         'my_normal': {
            'level': 'INFO',
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
root_logger = logging.getLogger(__name__) # this is a root logger
my_normal_logger = logging.getLogger('my_normal') # this is an `src` logger 
my_detailed_logger = logging.getLogger('my_detailed') # this is 'my_detailed' 

def main():
    root_logger.debug("hello from root logger")
    my_normal_logger.debug("won't print") # higher level needed
    my_normal_logger.info("hello from my_normal logger")
    my_detailed_logger.info("won't print") # higher level needed
    my_detailed_logger.warning("hello from my_detailed logger") 

    import animals.cat
    import animals.cow
    import animals.fish
    
if __name__ == '__main__':
    main()