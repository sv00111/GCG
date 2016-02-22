-- HOW TO USE THIS PROGRAM
-- 1. Place your word list as a .txt file in the same directory
--	  as this file.
-- 2. Load this file into GHCI
-- 3. Type randomWord "filename" to pick out a random word from
--    your file.

import Control.Monad
import System.IO
import System.Random
import Data.Char

randomWord :: String -> IO ()
randomWord file = do 
	nouns <- readIn file
	pickWord nouns
	return ()

readIn :: String -> IO [String]
readIn fileName = do
	contents <- readFile fileName
	let words = lines contents
	return words

pickWord :: [String] -> IO String
pickWord ws = do
	gen <- newStdGen
	let (index, newgen) = randomR (0, (length ws)-1) gen
	let word = (ws!!index)
	putStr $ word ++ "\n"
	return word