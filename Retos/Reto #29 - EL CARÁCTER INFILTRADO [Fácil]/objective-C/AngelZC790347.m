#import <Foundation/Foundation.h>

// clang -framework Foundation AngelZC790347.m && ./a.out && rm a.out	<-	Ejecutar

NSArray* filtrarCaracteres(NSString* frase1 ,NSString* frase2){
	NSMutableArray* result = [NSMutableArray new];
	if (frase1.length != frase2.length)
	{
		@throw [NSException exceptionWithName:NSInvalidArgumentException reason:@"Las frases deben ser de la misma longitud" userInfo:nil];
	}
	for (int i = 0; i < frase1.length; ++i)
	{
		if ([frase1 characterAtIndex:i] != [frase2 characterAtIndex:i])
		{
			unichar a = [frase2 characterAtIndex:i];
			[result addObject:[NSString stringWithCharacters:&a length:1]];
		}
	}
	return result;
}

int main()
{		
	@try{
		NSArray* res = filtrarCaracteres(@"Me llamo.Brais Moure", @"Me llamo brais moure");
		NSLog(@"%@",[res description]);
	}@catch(NSException* e){
		NSLog(@"%@",e.reason);
	}
	return 0;
}