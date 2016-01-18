---
layout: chapter
title: Building a Codebook
course: workshop

slides:

  - class: title-slide

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Building a Codebook
      _Take a look at codes through history_
      
      
      
  - content: |
  
        ## Semaphore
        
        ![Semaphore Letter R]([[BASE_URL]]/media/images/slidecontent/semaphore-r.png)
        
        With just two flags, how can we send a message?
        
    notes: |
        
        Let's start out easy - have you ever seen flags like this before? 
        
        Surf lifesavers? On the beach during the summer? Swim between the flags?
        
        Yes, they are used for that, but they can also be used to send messages.
        
        
  - content: |
  
      ## Semaphore A B Cs
      
      - ![Semaphore Letter A]([[BASE_URL]]/media/images/slidecontent/semaphore-a.svg){: width="150"}
      - ![Semaphore Letter B]([[BASE_URL]]/media/images/slidecontent/semaphore-b.svg){: width="150"}
      - ![Semaphore Letter C]([[BASE_URL]]/media/images/slidecontent/semaphore-c.svg){: width="150"}
      {: .flex-list }
      
      If this is A, B and C... what is D?
      
    notes: |
    
      So flinging flags around in different directions can make letters,
      but how can we remember which combination goes with each letter?
      
      Lucky for us, semaphore has a few patterns.
      
      Unlucky for us, there are also a few tricks!

      
  - content: |
  
      ## The Sensible Patterns in Semaphore
      
      The first half of the alphabet is reasonably logical:
      
      - ![Animation of Semaphore A to G]([[BASE_URL]]/media/images/slidecontent/semaphore-a-to-g.gif){: width="150"}
        **A to G**
        One arm straight down, the other ticking clockwise by 45 degrees for each letter.

      - ![Animation of Semaphore H to N]([[BASE_URL]]/media/images/slidecontent/semaphore-h-to-n.gif){: width="150"}
        **H to N**
        One arm to the bottom right, the other ticking clockwise by 45 degrees. Trick: Skip J!

      - ![Picture of Semaphore J]([[BASE_URL]]/media/images/slidecontent/semaphore-j.gif){: width="150"}
        **J**
        J is one arm straight up, one arm straight left. Weird, I know.
      {: .flex-list }
  
  
  - content: |
  
      ## The Less-Sensible Patterns in Semaphore
      
      The second half of the alphabet, not so logical:
      
      - ![Animation of Semaphore O to S]([[BASE_URL]]/media/images/slidecontent/semaphore-o-to-s.gif){: width="150"}
        **O to S**
        One arm right, the other ticking clockwise.
      - ![Animation of Semaphore T to Z]([[BASE_URL]]/media/images/slidecontent/semaphore-t-to-z.gif){: width="150"}
        **T to Z**
        Running out of combinations now, but same pattern.
      - ![Picture of Semaphore cancel signal]([[BASE_URL]]/media/images/slidecontent/semaphore-cancel.gif){: width="150"}
        **Ignore Message**
        Arms at top-right and bottom left, forming a slash symbol.    
      {: .flex-list }


  - content: |

      ## Add Semaphore to your Codebook

      Complete the Semaphore section of your codebook,
      so you can use it for the upcoming challenges.


  - content: |
  
      ## Semaphore Challenge

      ![Semaphore secret message]([[BASE_URL]]/media/images/slidecontent/semaphore-message.jpg)

      Decode the secret message.


  - content: |

      ## Who actually uses Semaphore?

      **Seamen**
      Widely adopted semaphore in the 1900s, 
      and it is still used for emergency communications. 
         
    notes: |

      Anyone in the Navy or other defence forces should be able to understand flag semaphore.

      Many emergency services people will also be familiar with it.

  
  - content: |
  
      ## Semaphore is great and all but...
      
      **What about long distance?**
      
      Semaphore is great for short-range visual communication, but quite often we want to send messages to people we can't actually see.
      
      
  - content: |
      
      ## Morse Code

      ![Morse Code Comic]([[BASE_URL]]/media/images/slidecontent/morse-code.gif)
      
      Dah-dah dah-dah-dah di-dah-dit di-di-dit dit.
      
      Srsly tho.
      
      
  - content: |
  
      ## Dots and Dashes
      
      All of morse code is made up of dots and dashes,
      which are communicated as long and short beeps.
      
      How do we know which dot and dash combination
      stands for each letter?
      

  - content: |
  
      ## Assigning Letters their Code

      We want to communicate as fast as possible, 
      so the letters we use most should have the shortest codes.
    
      
    notes: |
    
      Which is longer, a dot or a dash?
      
      If we had to choose which letter should be a dot and which should be a dash out of the letters A and Z, which would be the sensible way to assign them?
      
      Letters used more often should be given shorter codes. This way, all communications are as speedy as possible.


  - content: |
  
      ## Letters in Morse Code
      _Dots and Dashes_
      
      - ![Dash length equals three dots]([[BASE_URL]]/media/images/slidecontent/dot-and-dash-size.svg){: width="400"}
        A dash is three times 
        as long as a dot
      - ![Gap size equals one dot]([[BASE_URL]]/media/images/slidecontent/dot-dash-gap-size.svg){: width="400"}
      Each dot or dash is separated 
        by a gap the same length as a dot
      {: .flex-list }


  - content: |

      ## Letter Frequencies

      ![Chart of letter frequencies in English]([[BASE_URL]]/media/images/slidecontent/letter-frequencies.svg){: height="400" }

      This is a chart of the letter frequencies in the English language.

    notes: |

      If we were to design Morse code today, we would make `e` a single dot `.`, as it is the most common letter so should have the shortest code.

      Next would be `t` as it is next-most common. The letter `t` would be dot dot `..`

      Third is the letter `a`. A would be a single dash, which is the next shortest code.


  - content: |

      ## Letter Frequencies from Morse's Era

      Back when Mr Morse was around, 
      he calculated the letter frequencies as follows:

      ![Chart of letter frequencies from Morse's days]([[BASE_URL]]/media/images/slidecontent/old-letter-frequencies.svg){: width="700" }


  - content: |

      ## Build the Morse Code Chart

      ![Empty Morse Tree]([[BASE_URL]]/media/images/slidecontent/empty-morse-tree.svg){: width="700"}
      ![Chart of letter frequencies from Morse's days]([[BASE_URL]]/media/images/slidecontent/old-letter-frequencies.svg){: width="700" }

      Let's fill in the Morse Code chart using the letter frequencies.
  

  - content: |

      ## Add Morse Code to your Codebook

      Complete the Morse Code section of your codebook,
      so you can use it for the upcoming challenges.


  - content: |
  
      ## Communicating with Morse Code
      _Letters and Words_
      
      - ![Letter gap size equals three dots]([[BASE_URL]]/media/images/slidecontent/letter-gap-size.svg){: width="400"}
        Letters are separated by a gap 
        the same length as three dots
      - ![Word gap size equals seven dots]([[BASE_URL]]/media/images/slidecontent/word-gap-size.svg){: width="400"}
        Words are separated by a gap 
        the size of seven dots
      {: .flex-list }


  - content: |

      ## Morse Code Challenge
      
      Decode the secret message: Bunnies Love Chocolate


  - content: |

      ## Morse Code Game

      Listen to the Morse Code 
      and type the letter you hear.

      [Play Now](http://www.kongregate.com/games/dgreisen/morse)


  - content: |

      ## Morse Code is pretty cool too, but...
      
      **What about storing more complex data?**
      
      Morse Code is great for communicating quickly using words and numbers, but what about if you want to send sound or an image?


  - content: |

      ## Binary Code

      ![Binary XKCD Comic]([[BASE_URL]]/media/images/slidecontent/binary-xkcd.png)

      Hiding messages in bits of data.


  - content: |

      ## How big is a bit?

      At the most basic level, electronic things have two states:

      - ![Light bulb turned off]([[BASE_URL]]/media/images/slidecontent/bulb-off.png){: height="300" }
        **Off**
      - ![Light bulb turned on]([[BASE_URL]]/media/images/slidecontent/bulb-on.png){: height="300" }
        **On**
      {: .flex-list }

      That's a bit.


  - content: |

      ## Representing Bits

      - ![Zero and One]([[BASE_URL]]/media/images/slidecontent/zero-and-one.svg){: width="180" }
        0 and 1
      - ![White and Black]([[BASE_URL]]/media/images/slidecontent/white-and-black.svg){: width="180" }
        White and Black
      - ![Off and On]([[BASE_URL]]/media/images/slidecontent/off-and-on.svg){: width="180" }
        Off and On
      - ![Low and High]([[BASE_URL]]/media/images/slidecontent/low-and-high.svg){: width="180" }
        Low and High
      {: .flex-list }

      We can represent bits in lots of different ways, 
      but they all mean the same thing.


  - content: |

      ## Coding Letters in Binary

      ### A=1, B=2, C=3, D=4...

      How many bits would we need to code
      all of the letters from A to Z?


  - content: |

      ## Binary Combinations

      - ![One bit allows for two states ]([[BASE_URL]]/media/images/slidecontent/one-bit.svg){: height="300" }
        **One Bit**
        Two combinations
      - ![Two bits allow for four combinations ]([[BASE_URL]]/media/images/slidecontent/two-bits.svg){: height="300" }
        **Two Bits**
        Four combinations
      - ![Three bits allow for eight combinations ]([[BASE_URL]]/media/images/slidecontent/three-bits.svg){: height="300" }
        **Three Bits**
        Eight combinations
      {: .flex-list }

      Now can you figure out how many 
      bits we need for 26 letters?


  - content: |

      ## Counting in Binary

      ![Binary numbers 0 to 4]([[BASE_URL]]/media/images/slidecontent/binary-counting.svg)

      Can you see the pattern?


  - content: |

      ## Alphabet in Binary

      ![Binary letters A to D]([[BASE_URL]]/media/images/slidecontent/binary-alphabet.svg)

      We can make 1=A, 2=B, 3=C


  - content: |

      ## Add Binary to your Codebook

      Complete the Binary Alphabet section of your codebook,
      so you can use it for the upcoming challenges.


  - content: |

      ## Binary Challenge

      **01000**

      **01111**

      **01010**

      Decode the secret message


  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Codebook: Complete!

      Okay, now let's put our knowledge to the test...
      [Take me to the next chapter!](decoding.html)

    notes: |

      Okay, now let's put our knowledge to the test...
      

        
---     