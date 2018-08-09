function images = loadMNISTImages(filename)
%loadMNISTImages returns a 28x28x[number of MNIST images] matrix containing
%the raw MNIST images

fp = fopen(filename, 'rb');
assert(fp ~= -1, ['Could not open ', filename, '']);

magic = fread(fp, 1, 'int32', 0, 'ieee-be');
assert(magic == 2051, ['Bad magic number in ', filename, '']);

No_of_images = fread(fp, 1, 'int32', 0, 'ieee-be');
No_of_rows = fread(fp, 1, 'int32', 0, 'ieee-be');
No_of_columns = fread(fp, 1, 'int32', 0, 'ieee-be');

images = fread(fp, inf, 'unsigned char');
images = reshape(images, No_of_columns, No_of_rows, No_of_images);
images = permute(images,[2 1 3]);

fclose(fp);
%size(images) -> 28 28 60000
% Reshape to #pixels x #examples
images = reshape(images, size(images, 1) * size(images, 2), size(images, 3));
% Convert to double and rescale to [0,1]
images = double(images) / 255;

end
