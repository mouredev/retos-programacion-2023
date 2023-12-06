#import <Foundation/Foundation.h>
NSString* t9_transform(NSString*input){
	NSDictionary *dictionary = @{
		@0	:	@"¬",
       	@1 	: 	@"@",
    	@2 	: 	@"abc",
    	@3 	: 	@"def",
        @4 	: 	@"ghi",
        @5	:	@"jkl",
        @6	:	@"mno",
        @7	:	@"pqrs",
        @8	:	@"tuv",
        @9	:	@"wxyz",
	};
	NSArray * pattern = [input componentsSeparatedByString:@"-"];		
	NSMutableString * message = [[NSMutableString alloc] init];
	for (int i = 0; i < pattern.count; ++i)
	{		
		NSString * value= pattern[i];				
		NSNumber * key = [NSNumber numberWithInt:[[value substringToIndex:1] integerValue]];			
		[message appendFormat:@"%c",[dictionary[key] characterAtIndex:value.length-1]];
	}
	return message;
}

int main(int argc, char const *argv[])
{		
	NSLog(@"%@",t9_transform(@"6-666-88-777-33-3-33-888"));
	return 0;
}