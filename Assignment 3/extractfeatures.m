%%
% EXTRACTFEATURES( digdata )
%
% Arguments: 'digdata' is a 2-d matrix, size 16x16.
%
% Process the supplied 2d matrix to generate a lower dimensional
% feature vector, to be used in a learning algorithm.
%
% The returned vector is the sum of pixel values in each of the 16 columns.
% Alternatives might be the sum of values in the 16 rows, or combinations
% of the two, or other statistics of the pixels, like standard deviation.
%
% Note: This MUST return a 1-d array
%
%
function x = extractfeatures( digdata )

%sum the values in along matrix dimension 1 (rows)
x = sum(digdata,1);
