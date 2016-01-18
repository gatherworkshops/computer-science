---
layout: chapter
title: Data Representation
course: workshop

slides:

  - class: title-slide

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Data Representation
      _Storing stuff that's not just numbers_
      
      
      
  
  - content: |

      ## Bits and Bytes

      ![A byte is made up of 8 bits]([[BASE_URL]]/media/images/slidecontent/bits-and-bytes.svg){: height="300" }

      We usually use bits in groups of 8, allowing for numbers 
      large enough to cover most use cases.


  - content: |

      ## How "big" is a byte?

      ![Representing numbers using bits]([[BASE_URL]]/media/images/slidecontent/byte-size.svg)

      How many letters, numbers or symbols 
      could we represent with 8 bits?


  - content: |

      ## 8 bits gives us 256 combinations

      The lowest number we can store is zero...
      The largest number we can store is 255...
      There are 26 letters in the alphabet...

      **We can do _way_ more than just the alphabet!**


  - content: |

      ## So what can we store?

      Although each byte can only go as high as 255,
      we can store groups of bytes to make up more complex data.

  - content: |

      ## We'll look at

      - ![Numbers Icon]([[BASE_URL]]/media/images/slidecontent/numbers-icon.svg){: height="180"}
        **Numbers**
        Going beyond integers.
      - ![Documents Icon]([[BASE_URL]]/media/images/slidecontent/documents-icon.svg){: height="180"}
        **Documents**
        Letters and symbols.
      - ![Images Icon]([[BASE_URL]]/media/images/slidecontent/images-icon.svg){: height="180"}
        **Images**
        Colours in pixels.
      {: .flex-list }
  

  - content: |

      ## Numbers

      How do we describe a number that's not an integer?


  - content: |

      ## Negative Numbers

      We usually set aside the leftmost bit 
      to represent positive or negative.


  - content: |

      ## Decimals

      ???


  - content: |

      ## Challenge

      Decode the three numbers


  - content: |

      ## ASCII

      ![ASCII Cat]([[BASE_URL]]/media/images/slidecontent/ascii-art.png){: height="240"}

      The ASCII format is a way of storing letters, 
      numbers and symbols used in blocks of text.

      Many `.txt` files are stored in the ASCII format.

    notes: |

      We pronounce ASCII as "Ass-key", but it's actually short for "American Standard Code for Information Interchange".


  - content: |

      ## ASCII Alphabet

      Long story short:

      - A-Z is 65-90
      - a-z is 97-122

      Can you see a pattern? Hide the 3 leftmost bits of each column...


  - content: |

      ## Big vs Little

      That means that the only difference between uppercase letters and lowercase letters is a single bit!

  - content: |

      ## ASCII Numbers

      Look! It's the same pattern again!

      The **characters** 0-9 don't map to the binary **numbers** 0-9, but they still follow an easily recognisable pattern.


  - content: |

      ## ASCII Special Characters

      No pattern here, but only because symbols don't have a natural order.

    notes: |

      Look at your keyboard though - how many of the symbols in the ASCII table line up with the symbols above the numbers on your keyboard?

  
  - content: |

      ## Challenge

      Decode the ASCII text file


  - content: |

      ## Images

      ![Close-up of the pixels in a photograph]([[BASE_URL]]/media/images/slidecontent/photo-pixels.jpg)

      Most images contain millions of pixels

    notes: |

      All digital images are made up of pixels.

      We talk about cameras having a certain number of "megapixels". A megapixel is a _million_ pixels!


  - content: |

      ## Bitmap Images

      ![Pixel Art: Mario, Luigi, Peach and Toad by Hama-Girl]([[BASE_URL]]/media/images/slidecontent/mario-pixel-art.png)
      <!-- .element height="350" -->

      In smaller images such as pixel art, there are fewer colour points to be stored.

  - content: |

      ## Black and White

      The most simple image we can represent would be black and white:
      one bit for every pixel.


  - content: |

      ## Image Size

      1101010001010010100001010110101010
      1010101010010101010100101010101010
      11101010110101001

      In the computer, all the bits are stored in a long line.
      How do we know how wide and how high the image should be?

  - content: |

      ## File Headers

      We can add some extra bits at the start of the file
      to record the image's width and height.

  - content: |

      ## Challenge

      Set the image to the correct dimensions.

  - content: |

      ## Colours

      // 1-bit 2-bit 4-bit 8-bit 16-bit

      The number of colour options we have for each pixel is determined by
      the number of bits we allow for each pixel.

  - content: |

      ## 24bit Images

      A 24bit image gives each pixel three bytes to store its colour.
      One byte for red, one for green, and one for blue.


  - content: |

      ## Challenge

      Complete the binary crossword.
      Yes, it's ridiculous. Enjoy!


  - content: |

      ## Bonus Challenge

      <iframe width="560" height="315" src="https://www.youtube.com/embed/L-v4Awj_p7g" frameborder="0" allowfullscreen></iframe>

      **Find as many hidden messages as you can in this video.**

      Do this one in your own time if you feel like a challenge!


  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Data Representation: Complete!

      Now we can work on encrypting our secret data...
      [Take me to the next chapter!](encryption.html)

    notes: |

      Now we can work on encrypting our secret data...
      

        
---     