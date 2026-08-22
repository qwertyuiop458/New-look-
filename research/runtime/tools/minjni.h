/* Минимальный jni.h — только объявления, нужные для libaudio stub.
   (Полный JNI-заголовок недоступен: JRE без include/; jni.h не требуется
   для пустых JNI-функций, но нужен тип JNIEnv.) */
#ifndef _MIN_JNI_H_
#define _MIN_JNI_H_

typedef struct JNINativeInterface_ JNINativeInterface;
typedef const struct JNINativeInterface_ *JNIEnv;
typedef struct _jclass *jclass;
typedef struct _jobject *jobject;
typedef int jint;

#endif

#define JNIEXPORT __attribute__((visibility("default")))
#define JNICALL
