;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.

(define fact(lambda (n)
              (if (= n 1)
                 1
                   (* fact(- n 1) n))))

(define fib(lambda (n)
             (if (= n 0)
                0
                (if (= n 1)
                   1
                   (+ (fib(- n 1) fib(- n 2)))))))
