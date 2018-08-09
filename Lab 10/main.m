
%Load file
load cancer.mat;

% %Actual -> class labels
% actual = dataset(:,10);

%Split dataset into two.. half -> 350
half = floor(length(dataset)/2);

%For first fold
training = dataset(1:half,1:9);
training_labels = dataset(1:half,10);

testing = dataset(half+1:length(dataset),1:9);
testing_labels = dataset(half+1:length(dataset),10);
a = 1;
for k = 1:2:20

    for i = 1:length(testing)
    
        sample = testing(i,:);
        [r,c] = size(training);
        distance=zeros(r,1);
        for j = 1:r
            distance(j,1) = sqrt(sum((sample - training(j)).^2));       
        end

        [s, index] = sort(distance);
        temp_label = training_labels(index(1:k));
        
        index1 = 0;
        index2 = 0;
        
        if (temp_label == 0)
            index1 = index1+1;
        else
            index2 = index2+1;
        end
%         sorted = sort(distance);
%         max_value = max(sorted(1:k));
%         temp_label = training_labels(distance <= max_value);
%         total_ones = sum(temp_label);
%         total_zeros = length(temp_label) - total_ones;
%     
%         if total_ones >= total_zeros
%             predicted(i) = 1;
%         else
%             predicted(i) = 0;
%         end
         
    end
    
        Correctly_Predicted = sum((transpose(predicted) - testing_labels) == 0);
        
        Accuracy(a) = 100*(Correctly_Predicted/length(testing_labels));
        a = a + 1;
end

k = 1:2:20;
plot(k, Accuracy)

Accuracy
